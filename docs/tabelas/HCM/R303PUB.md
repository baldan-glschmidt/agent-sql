# R303PUB

## Descrição

e-Sfinge - Módulo Genérico/Publicidade

---

## Resumo

- Campos: 11
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| AnoBas | Number(004,0) | Não | Ano |
| BimAno | Number(001,0) | Não | Código Bimestre Ano |
| TipTex | Number(002,0) | Não | Tipo do texto jurídico |
| NumTex | String(016) | Não | Número do texto jurídico |
| DatPub | Date | Não | Data em que foi publicado o ato jurídico |
| NumSeq | Number(002,0) | Não | Número sequencial |
| MeiCom | Number(002,0) | Não | Tipo do meio de comunicação |
| VeiCom | String(100) | Sim | Nome do veículo de comunicação |
| ReaPra | String(001) | Não | Publicação acarreta nova contagem prazo para atos com contagem de prazos legais |
| OriReg | String(001) | Sim | Origem do Registro (G-Gerado, D-Digitado, I-Importado) |

---

## Chave Primária

- NumEmp
- AnoBas
- BimAno
- TipTex
- NumTex
- DatPub
- NumSeq

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
