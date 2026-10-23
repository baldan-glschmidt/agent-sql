# R038AFF

## Descrição

Afastamentos - Férias Coletivas eSocial

---

## Resumo

- Campos: 10
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Colaborador |
| DatAfa | Date | Não | Data do Afastamento |
| HorAfa | Number(005,0) | Não | Hora do Afastamento |
| SeqReg | Number(002,0) | Não | Sequencia do Registro |
| IniFer | Date | Sim | Data Início das Férias |
| FimFer | Date | Sim | Data Fim das Férias |
| IniPer | Date | Sim | Data Início do Período Aquisitivo |
| FimPer | Date | Sim | Data Fim do Período Aquisitivo |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatAfa
- HorAfa
- SeqReg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R038AFF_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R038AFF_004

**Tabela:** R038AFA

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| DatAfa | DatAfa |
| HorAfa | HorAfa |

