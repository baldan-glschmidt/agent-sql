# R070MSC

## Descrição

Mensagem para Colaborador

---

## Resumo

- Campos: 11
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Colaborador |
| DatIni | Date | Não | Data Inicial da Mensagem |
| HorIni | Number(005,0) | Não | Hora Inicial da Mensagem |
| DatFim | Date | Sim | Data Inicial da Mensagem |
| HorFim | Number(005,0) | Sim | Hora Final da Mensagem |
| QtdMsg | Number(002,0) | Sim | Qtde de Vezes que Será Mostrada a Mensagem nos Relógios |
| MsgAcc | String(032) | Sim | Descrição da Mensagem que Será Mostrada nos Coletores |
| StaAcc | Number(001,0) | Sim | Status da Mensagem |
| CodUsu | Number(009,0) | Sim | Código do usuário que cadastrou a mensagem |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatIni
- HorIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R070MSC_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

