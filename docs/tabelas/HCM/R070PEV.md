# R070PEV

## Descrição

Permissão Alternativa Visitante

---

## Resumo

- Campos: 14
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TipDoc | Number(001,0) | Não | Tipo de Documento |
| NumDoc | String(020) | Não | Número do Documento |
| DatIni | Date | Não | Data Inicial da Permissão Alternativa |
| HorIni | Number(005,0) | Não | Hora Inicial da Permissão Alternativa |
| CodPrm | Number(005,0) | Não | Código da Permissão Alternativa |
| DatFim | Date | Sim | Data Final da Permissão Alternativa |
| HorFim | Number(005,0) | Sim | Hora Final da Permissão Alternativa |
| CodUsu | Number(010,0) | Sim | Código do Usuário que Cadastrou a Permissão |
| NumEmp | Number(004,0) | Sim | Empresa do Responsável |
| TipCol | Number(001,0) | Sim | Tipo Responsável |
| NumCad | Number(009,0) | Sim | Cadastro do Responsável |
| ObsPrm | String(080) | Sim | Observação |
| StaAcc | Number(001,0) | Sim | Status da Área Restrita |
| SeqReg | Number(015,0) | Sim | Sequencia do Registro |

---

## Chave Primária

- TipDoc
- NumDoc
- DatIni
- HorIni
- CodPrm

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R070PEV_001

**Tabela:** R090VIS

| Origem | Destino |
|--------|---------|
| TipDoc | TipDoc |
| NumDoc | NumDoc |

### IR_R070PEV_004

**Tabela:** R058PRM

| Origem | Destino |
|--------|---------|
| CodPrm | CodPrm |

