# Desafio Final Cloud Computing - Turma 12DVP

### Integrantes:

- PEDRO CARDENETE VICENTE – RM 343560
- PAULO HENRIQUE NUNES VANDERLEY – RM 343889
- WAGNER EDUARDO PEREIRA – RM 342643


[Link GitHub](https://github.com/PedroCardenete/cloud-computing-12DVP)

## (Opcional) Instalar ambiente local para execução do Serverless Framework. 

Para preparar o ambiente local, executar o script abaixo. 

```
./install-local/install.sh
```

## Imagens da aplicação em funcionamento.

### 1. Realizado o deploy da Lambda e S3 na AWS via Serverless Framework. Nota: DynamoDB criado manualmente via Console. 

![image info](./.images/image1.png)

![image info](./.images/image1.2.png)

![image info](./.images/image1.3.png)

### 2. Criação de arquivo json e upload para o S3.  

![image info](./.images/image2.png)

### 3. Upload com sucesso no S3. 

![image info](./.images/image3.png)

### 4. Log do CloudWatch registrando a trigger no Lambda monitorjpgppw-dev-getObject.

![image info](./.images/image4.png)

### 5. Registro do json no DynamoDB como ativo igual a True (criado). 

![image info](./.images/image5.png)

### 6. Deleção do arquivo json no S3. 

![image info](./.images/image6.png)

### 7. Log do CloudWatch registrando a trigger no Lambda monitorjpgppw-dev-removeObject.

![image info](./.images/image7.png)

### 8. Registro do json no DynamoDB como ativo igual a False (deletado). 

![image info](./.images/image8.png)
