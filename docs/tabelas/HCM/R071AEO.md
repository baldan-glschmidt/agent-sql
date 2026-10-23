# R071AEO

## Descrição

Autorização de Entrada - Outras Unidades

---

## Resumo

- Campos: 9
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador de Outra Unidade |
| DatEnt | Date | Não | Data de Início da Autorização de Entrada |
| HorEnt | Number(005,0) | Não | Hora de Início da Autorização de Entrada |
| DatVal | Date | Sim | Data de Validade da Autorização |
| HorVal | Number(005,0) | Sim | Hora de Validade da Autorização |
| DatSai | Date | Sim | Data da Saída do Colaborador |
| HorSai | Number(005,0) | Sim | Hora da Saída do Colaborador |
| ObsAEn | String(080) | Sim | Observação da Autorização de Entrada |

---

## Chave Primária

- NumEmp
- NumCad
- DatEnt
- HorEnt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R071AEO_001

**Tabela:** R070OCR

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| NumCad | NumCad |

