# R108ANX

## Descrição

Anexos de Exames

---

## Resumo

- Campos: 9
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da empresa |
| CodFic | Number(009,0) | Não | Código Ficha Médica |
| CodExa | Number(004,0) | Não | Código do exame |
| DatSol | Date | Não | Data Solicitação do Exame |
| SeqAne | Number(002,0) | Não | Sequência do anexo |
| DesAne | String(030) | Sim | Descrição do arquivo anexo |
| DocAne | Image | Sim | Documento |
| NomAne | String(250) | Sim | Nome do arquivo anexo |
| SitAss | Number(001,0) | Sim | Status da assinatura digital do documento |

---

## Chave Primária

- NumEmp
- CodFic
- CodExa
- DatSol
- SeqAne

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
