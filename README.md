## Amazon SageMaker NLU search

This repository guides users through creating a NLU based product search using Amazon SageMaker and Amazon Elasticsearch service


## How does it work?

we have used pre-trained BERT model(distilbert-base-nli-stsb-mean-tokens) from sentence-transformers to generate fixed 768 length sentence embedding on Multi-modal Corpus of Fashion Images from *__feidegger__*, a *__zalandoresearch__* dataset. Then those feature vectors is imported in Amazon ES KNN Index as a reference.

![diagram](../master/ref.png)


When we present a new query text/sentence, it's computing the related embedding from Amazon SageMaker hosted BERT model and query Amazon ES KNN index to find similar text/sentence and corresponds to the actual product image which is stored in Amazon S3

![diagram](../master/query.png)

## License

This library is licensed under the MIT-0 License. See the LICENSE file.
