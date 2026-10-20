# Instruções do projeto Agent SQL

## 1. Objetivo

Este projeto é utilizado para análise, consulta e desenvolvimento de scripts
SQL relacionados ao banco de dados do sistema.

A IA deve priorizar informações existentes na documentação do próprio projeto
e evitar assumir estruturas de banco que não estejam documentadas.

---

## 2. Fonte oficial da estrutura das tabelas

Os arquivos localizados em:

`docs/Arquivo TBS/`

são a fonte oficial para consultar a estrutura das tabelas do banco.

Esses arquivos contêm informações sobre:

- tabelas;
- campos;
- tipos de dados;
- descrições;
- relacionamentos;
- informações relacionadas à estrutura do banco.

Sempre que uma solicitação envolver a identificação de uma tabela ou campo,
consulte primeiro os arquivos dessa pasta.

Não invente nomes de tabelas ou campos.

Não utilize conhecimento genérico sobre bancos de dados para assumir que
uma tabela ou campo existe.

Se a informação não for encontrada na documentação TBS, informe claramente
que ela não foi localizada.

---

## 3. Arquivos SQL

Os arquivos localizados em:

`sql/`

contêm scripts e procedimentos utilizados no projeto.

Utilize esses arquivos para entender:

- regras de negócio;
- consultas existentes;
- procedimentos;
- funções;
- joins;
- filtros;
- lógica de processamento;
- padrões já utilizados no projeto.

Os arquivos SQL podem ser utilizados para entender COMO uma informação é
processada, mas a documentação em `docs/Arquivo TBS/` deve ser considerada
a fonte oficial para determinar a estrutura das tabelas.

---

## 4. Ordem de consulta

Quando uma solicitação envolver banco de dados, siga preferencialmente esta
ordem:

1. Consultar `docs/Arquivo TBS/` para identificar tabelas e campos.
2. Consultar `sql/` para verificar como essas tabelas são utilizadas no projeto.
3. Consultar outras partes do projeto somente quando necessário para entender
   o contexto da solicitação.

---

## 5. Validação

Antes de gerar uma query SQL:

1. Verifique se as tabelas utilizadas existem na documentação TBS.
2. Verifique se os campos utilizados existem na documentação TBS.
3. Verifique se os relacionamentos utilizados fazem sentido.
4. Quando existir um exemplo equivalente em `sql/`, considere o padrão já
   utilizado no projeto.
5. Se houver dúvida ou conflito entre informações, informe o conflito em vez
   de assumir uma resposta.

---

## 6. Não inventar estrutura

Nunca crie uma query utilizando campos ou tabelas apenas porque seus nomes
parecem coerentes.

Exemplo:

Se a documentação possui:

`E075PRO.CODPRO`

não assuma que exista:

`E075PRO.DESPRO`

sem verificar a documentação.

Caso um campo necessário não seja encontrado, informe:

"Não localizei esse campo na documentação TBS."

---

## 7. SQL existente

Antes de criar uma solução completamente nova, procure nos arquivos SQL
existentes por implementações semelhantes.

Quando encontrar uma implementação existente:

- reutilize padrões;
- mantenha a mesma lógica quando aplicável;
- evite criar soluções diferentes sem necessidade;
- informe quando estiver reutilizando uma lógica existente.

---

## 8. Respostas

Ao apresentar uma solução SQL, informe brevemente:

- quais tabelas foram utilizadas;
- quais campos principais foram utilizados;
- de onde essas informações foram obtidas;
- eventuais suposições ou pontos que precisam de validação.

Não altere arquivos do projeto sem que isso seja solicitado.