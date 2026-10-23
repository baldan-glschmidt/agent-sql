# R070PEO

## Descrição

Permissão Alternativa Outra Unidade

---

## Resumo

- Campos: 10
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| NumCad | Number(009,0) | Não | Cadastro Colaborador |
| DatIni | Date | Não | Data Inicial da Permissão Alternativa |
| HorIni | Number(005,0) | Não | Hora Inicial da Permissão Alternativa |
| CodPrm | Number(005,0) | Não | Código da Permissão Alternativa |
| DatFim | Date | Sim | Data Final da Permissão Alternativa |
| HorFim | Number(005,0) | Sim | Hora Final da Permissão Alternativa |
| CodUsu | Number(010,0) | Sim | Código do Usuário que Cadastrou a Permissão |
| ObsPrm | String(080) | Sim | Observação |
| StaAcc | Number(001,0) | Sim | Status da Área Restrita |

---

## Chave Primária

- NumEmp
- NumCad
- DatIni
- HorIni
- CodPrm

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R070PEO_001

**Tabela:** R070OCR

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| NumCad | NumCad |

### IR_R070PEO_004

**Tabela:** R058PRM

| Origem | Destino |
|--------|---------|
| CodPrm | CodPrm |

