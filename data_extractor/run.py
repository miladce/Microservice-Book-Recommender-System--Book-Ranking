from app.pipeline_runners.actions import strategy as actions_strategy
from app.pipeline_runners.books import strategy as books_strategy
from app.src.pipeline import Pipeline

if __name__ == '__main__':
    pipe = Pipeline(books_strategy)
    pipe.run(checkpoint_file='checkpoints/books.chkp')
    pipe = Pipeline(actions_strategy)
    pipe.run(checkpoint_file='checkpoints/actions.chkp')

