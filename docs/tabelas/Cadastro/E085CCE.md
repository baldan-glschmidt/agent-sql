# E085CCE

## Descrição

Cadastros - Clientes - Ligação Cliente X Tipos de Contas X Eventos

---

## Resumo

- Campos: 11
- Chave Primária: 5 campo(s)
- Índices: 2
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodCli | Number(009,0) | Não | Código do Cliente |
| CodTcc | String(003) | Não | Código do tipo de conta |
| NumCco | String(014) | Não | Número da Conta Interna |
| CodEtc | Number(004,0) | Não | Código do Evento |
| DatMov | Date | Sim | Data Movimento |
| ObsCce | String(250) | Sim | Observação da ligação |
| UsuGer | Number(010,0) | Sim | Código do usuário responsável pelo geração do registro |
| DatGer | Date | Sim | Data de geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| SitCce | String(001) | Sim | Indicativo da situação |

---

## Chave Primária

- CodEmp
- CodCli
- CodTcc
- NumCco
- CodEtc

---

## Índices

### E085CCEIndice1

**Tipo:** Não unico

Campos:
- CodCli

### E085CCEIndice2

**Tipo:** Não unico

Campos:
- CodTcc

---

## Relacionamentos

### IR_E085CCE_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

### IR_E085CCE_001

**Tabela:** E085CLI

| Origem | Destino |
|--------|---------|
| CodCli | CodCli |

### IR_E085CCE_002

**Tabela:** E034TCC

| Origem | Destino |
|--------|---------|
| CodTcc | CodTcc |

