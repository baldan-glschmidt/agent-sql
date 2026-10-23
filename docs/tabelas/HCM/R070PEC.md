# R070PEC

## Descrição

Permissão Alternativa Colaborador

---

## Resumo

- Campos: 13
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
| DatIni | Date | Não | Data Inicial da Permissão Alternativa |
| HorIni | Number(005,0) | Não | Hora Inicial da Permissão Alternativa |
| CodPrm | Number(005,0) | Não | Código da Permissão Alternativa |
| DatFim | Date | Sim | Data Final da Permissão Alternativa |
| HorFim | Number(005,0) | Sim | Hora Final da Permissão Alternativa |
| CodUsu | Number(010,0) | Sim | Código do Usuário que Cadastrou a Permissão |
| ObsPrm | String(080) | Sim | Observação |
| StaAcc | Number(001,0) | Sim | Status da Área Restrita |
| SeqReg | Number(015,0) | Sim | Sequencia do Registro |
| OriDef | Number(001,0) | Sim | Origem da Definição |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatIni
- HorIni
- CodPrm

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R070PEC_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R070PEC_005

**Tabela:** R058PRM

| Origem | Destino |
|--------|---------|
| CodPrm | CodPrm |

