# R060PDS

## Descrição

Perda DSR Definições da Integração

---

## Resumo

- Campos: 5
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodSit | Number(003,0) | Não | Código da Situação de Perda DSR |
| ComFal | String(001) | Não | Competência da Falta |
| TipLim | String(001) | Não | Tipo de Limite da Situação de Falta |
| LimFal | Number(005,0) | Sim | Limite de Horas da Situação de Falta |

---

## Chave Primária

- NumEmp
- CodSit
- ComFal
- TipLim

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R060PDS_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R060PDS_001

**Tabela:** R010SIT

| Origem | Destino |
|--------|---------|
| CodSit | CodSit |

