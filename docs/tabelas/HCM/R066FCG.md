# R066FCG

## Descrição

Fila de cálculo do GPO Lite

---

## Resumo

- Campos: 16
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| TipFcg | Number(001,0) | Não | Tipo do Registro na fila |
| DatGer | Date | Não | Data em que foi gerado o registro na fila |
| HorGer | Number(005,0) | Sim | Hora de Geração do Registro na Fila |
| DatApu | Date | Não | Data da Apuração |
| DatAfa | Date | Sim | Data do Afastamento |
| HorAfa | Number(005,0) | Sim | Hora do Afastamento |
| CodUsu | Number(010,0) | Sim | Código do Usuário do Processamento |
| StaFcg | Number(001,0) | Sim | Status do Registro na Fila |
| DatAtu | Date | Não | Data Última Atualização do Registro na Fila |
| HorAtu | Number(005,0) | Não | Hora Última Atualização do Registro na Fila |
| DatPro | Date | Sim | Data Processamento do Registro na Fila |
| HorPro | Number(005,0) | Sim | Hora Processamento do Registro na Fila |
| QtdTen | Number(002,0) | Sim | Quantidade Tentativas nas Execuções |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- TipFcg
- DatApu

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
