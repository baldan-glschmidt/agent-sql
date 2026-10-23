# R070PEA

## Descrição

Permissão Alternativa Aluno

---

## Resumo

- Campos: 9
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumMat | String(015) | Não | Matrícula do Aluno |
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

- NumMat
- DatIni
- HorIni
- CodPrm

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R070PEA_000

**Tabela:** R073ALU

| Origem | Destino |
|--------|---------|
| NumMat | NumMat |

### IR_R070PEA_003

**Tabela:** R058PRM

| Origem | Destino |
|--------|---------|
| CodPrm | CodPrm |

