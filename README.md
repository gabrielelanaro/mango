# Intro

Mango-ml is a machine learning framework designed for fast experimentation.

Mango provides a set of interfaces and guidelines to build and maintain
machine learning models, including support for logging and keeping track
of parameters between runs.

# Quick start

Mango has a bunch of useful abstractions that encourage separation of concerns
and code reuse:

- Model
- Dataset
- Loader
- Reporter
- Experiment

The following file represent a complete project structure for mango. 


```
import mango

class Dataset(mango.Dataset):
  seed = mango.Param(int, default=0)
  
  def build(self):
      random.seed(self.seed)
      X, y = make_classification()
      self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y)
      
  def train(self):
      self.data = self.X_train, self.y_train
      
  def eval(self):
      self.data = self.X_test, self.y_test
      
      
class Model(mango.Model):
  alpha = mango.Param(float)
  
  def build(self):
      self.clf = LogisticRegression(alpha=self.alpha)

  def train(self, loader):
      X, y = loader.train()
      
      self.clf.fit(X, y)
  
  def eval(self, loader):
      X,  y = loader.eval()
      self.reporter.add_scalar("score", self.clf.score(X, y))
      
      self.reporter.log('Saving model')
      with self.context['experiment'].file('file.pickle') as fd:
        pickle.dump(fd, self.clf)
       
      
class Main(mango.Experiment):
  
  reporter = mango.CombinedReporter([LogReporter(), TextReporter()])
  model = Model(alpha=0.5)
  dataset = Dataset()
  loader = SimpleLoader(dataset)
  trainer = SimpleTrainer(model, loader)
  
```

Once we defined our Experiment, we can run it using the following command:

```
mango train example.Main
```


## Improving code structure

In this section we will see how to train a machine learning system with mango. While mango doesn't enforce a particular file structure, a good standard is to use a typical python package layout. In this example, we will create a package structure containing the models, experiments and datasets modules. 

```
hello/
 README
 hello/
    __init__.py
    models.py
    experiments.py
    datasets.py
```

The entry point for a mango application is the Experiment.


