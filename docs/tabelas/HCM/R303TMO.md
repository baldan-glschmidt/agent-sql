# R303TMO

## Descrição

e-Sfinge - Terceirização de Serviços com Disponibilização de Mão de Obra

---

## Resumo

- Campos: 8
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| AnoBas | Number(004,0) | Não | Ano |
| BimAno | Number(001,0) | Não | Código Bimestre Ano |
| AnoMes | Date | Não | Mês e Ano dos dados relativos a terceirização |
| NomPos | String(100) | Não | Nome do Posto de Trabalho/Categoria/Função |
| QtdPos | Number(008,0) | Não | Quantidade de Postos de Trabalho/Categoria/Função |
| ValDes | Number(014,2) | Não | Valor da Despesa Liquidada |
| OriReg | String(001) | Sim | Origem do Registro (G-Gerado, D-Digitado, I-Importado) |

---

## Chave Primária

- NumEmp
- AnoBas
- BimAno
- AnoMes
- NomPos

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
