# R303TXJ

## Descrição

e-Sfinge - Módulo Genérico/Texto Jurídico

---

## Resumo

- Campos: 11
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
| TipTxj | Number(002,0) | Não | Tipo do texto jurídico |
| NumTxj | String(016) | Não | Número do texto jurídico |
| NatTxj | Number(002,0) | Não | Natureza do Texto Jurídico |
| DscEme | String(255) | Não | Descrição da Ementa |
| IndLOR | String(001) | Não | Indica se a legislação é a original |
| NumLAU | String(016) | Sim | Identifica n. da lei que autoriza regulamentação por tipo de legislação inferior |
| DatLAU | Date | Sim | Data de publicação da lei autorizativa |
| OriReg | String(001) | Sim | Origem do Registro (G-Gerado, D-Digitado, I-Importado) |

---

## Chave Primária

- NumEmp
- AnoBas
- BimAno
- TipTxj
- NumTxj

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
