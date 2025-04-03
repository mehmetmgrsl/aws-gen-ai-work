### What is Amazon Bedrock

It is used to build and scale generative AI applications with foundation models (1*)

### Test Amazon Titan-text-express Model (2*)

- AWS_REGION is set to 'eu-central-1'

- python bedrock_simple_demo.py -> This Python script uses the Amazon Titan Text Express model via the Bedrock service to generate a text response (such as a list of 90s music bands in Germany) based on a user-provided prompt

- Run -> ```python bedrock_simple_demo.py```

- Response:

```
INFO:__main__:Generating text with Amazon &titan-text-express; model amazon.titan-text-express-v1
INFO:botocore.credentials:Found credentials in environment variables.
INFO:__main__:Successfully generated text with Amazon &titan-text-express; model amazon.titan-text-express-v1
Input token count: 19
Token count: 53
Output text: 
Here are five unique German music bands active in the 1990s:
1. The Notwist
2. Die Fantastischen Vier
3. Die Ärzte
4. Rammstein
5. Die Toten Hosen
Completion reason: FINISH
Finished generating text with the Amazon &titan-text-express; model amazon.titan-text-express-v1.
```

### List Amazon's Foundation Models in eu-central-1

Run -> ```python list-foundation-models.py```

Response:

```
Titan Text G1 - Express : amazon.titan-text-express-v1:0:8k
Titan Text G1 - Express : amazon.titan-text-express-v1
Titan Text G1 - Lite : amazon.titan-text-lite-v1:0:4k
Titan Text G1 - Lite : amazon.titan-text-lite-v1
Titan Embeddings G1 - Text : amazon.titan-embed-text-v1:2:8k
Titan Embeddings G1 - Text : amazon.titan-embed-text-v1
Titan Multimodal Embeddings G1 : amazon.titan-embed-image-v1:0
Titan Multimodal Embeddings G1 : amazon.titan-embed-image-v1
Titan Embeddings G2 - Text : amazon.titan-embed-text-v2:0
Rerank 1.0 : amazon.rerank-v1:0
Nova Pro : amazon.nova-pro-v1:0
Nova Lite : amazon.nova-lite-v1:0
Nova Micro : amazon.nova-micro-v1:0
```

### References

1* https://aws.amazon.com/bedrock/

2* https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-titan-text.html