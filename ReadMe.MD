### What is Amazon Bedrock

It is used to build and scale generative AI applications with foundation models (1*)

### Test Amazon Titan-text-express Model (2*)

AWS_REGION is set to 'eu-central-1'

Run -> ```python bedrock_simple_demo.py```

Response:

```
INFO:__main__:Generating text with Amazon &titan-text-express; model amazon.titan-text-express-v1
INFO:botocore.credentials:Found credentials in environment variables.
INFO:__main__:Successfully generated text with Amazon &titan-text-express; model amazon.titan-text-express-v1
Input token count: 14
Token count: 155
Output text: 
Here is a list of 80's music bands in Germany:
1. Nena
2. Falco
3. Modern Talking
4. Alphaville
5. Culture Beat
6. Tocotronic
7. Die Toten Hosen
8. Ideal
9. Extrabreit
10. DAF
11. Fun Factory
12. La Düsseldorf
13. Spider Murphy Gang
14. Münchener Freiheit
15. Joachim Witt
16. Captain Jack
17. Silbermond
18. Die Fantastischen Vier
19. Die Ärzte
20. Trio
Completion reason: FINISH
Finished generating text with the Amazon &titan-text-express; model amazon.titan-text-express-v1.
```

### List Amazon's Foundation Models in eu-central-1

Run -> ```python list-foundation-models.py```

Response:

```
Titan Text G1 - Express : amazon.titan-text-express-v1:0:8k
Titan Text G1 - Express : amazon.titan-text-express-v1
Titan Embeddings G1 - Text : amazon.titan-embed-text-v1:2:8k
Titan Embeddings G1 - Text : amazon.titan-embed-text-v1
```

### References

1* https://aws.amazon.com/bedrock/

2* https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-titan-text.html