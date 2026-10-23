# R038PRO

## Descrição

Afastamentos - Prorrogações

---

## Resumo

- Campos: 12
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Colaborador |
| DatAfa | Date | Não | Data do Afastamento |
| HorAfa | Number(005,0) | Não | Hora do Afastamento |
| DatIni | Date | Não | Data de início da prorrogação |
| NumAto | Number(007,0) | Sim | Número do Ato de Prorrogação |
| NumLau | Number(002,0) | Sim | Número do Laudo Médico |
| DatPub | Date | Sim | Data da publicação do ato |
| DatTer | Date | Sim | Data de término da prorrogação |
| NumBol | Number(006,0) | Sim | Número do Boletim |
| ObsPro | String(799) | Sim | Observação |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatAfa
- HorAfa
- DatIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R038PRO_004

**Tabela:** R038AFA

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| DatAfa | DatAfa |
| HorAfa | HorAfa |

