from transformers import pipeline

# classifier = pipeline('sentiment-analysis')
# res = classifier(
#     'We are not very happy to introduce pipeline to the transformers repository.')

pipe = pipeline('question-answering')
res = pipe({
    'question': 'What is the name of the repository ?',
    'context': 'Pipeline have been included in the huggingface/transformers repository'
})

print(res)
