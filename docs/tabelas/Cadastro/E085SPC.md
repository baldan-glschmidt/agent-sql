# E085SPC

## Descrição

Cadastros - Clientes  - Consultas ao SPC

---

## Resumo

- Campos: 11
- Chave Primária: 1 campo(s)
- Índices: 4
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador único |
| CodCli | Number(009,0) | Não | Código do Cliente |
| DatCon | Date | Não | Data da consulta |
| IdeCae | Number(009,0) | Não | Identificador único da consulta |
| InfSpc | Number(001,0) | Não | Situação junto ao SPC |
| UsuCon | Number(010,0) | Não | Usuário responsável pela consulta |
| EmpCon | Number(004,0) | Não | Empresa da filial responsável pela consulta |
| FilCon | Number(005,0) | Não | Filial responsável pela consulta |
| SeqCon | Number(009,0) | Não | Sequência da consulta na filial responsável pela consulta |
| ReqCon | String(50000) | Sim | Dados de requisição da consulta |
| RetCon | String(50000) | Sim | Dados de retorno da consulta |

---

## Chave Primária

- IdeUni

---

## Índices

### E085SPCUnique

**Tipo:** Não unico

Campos:
- CodCli
- FilCon
- SeqCon
- IdeCae

### E085SPCIndice2

**Tipo:** Não unico

Campos:
- CodCli

### E085SPCIndice3

**Tipo:** Não unico

Campos:
- IdeCae

### E085SPCIndice4

**Tipo:** Não unico

Campos:
- EmpCon
- FilCon

---

## Relacionamentos

### IR_E085SPC_001

**Tabela:** E085CLI

| Origem | Destino |
|--------|---------|
| CodCli | CodCli |

### IR_E085SPC_003

**Tabela:** E085CAE

| Origem | Destino |
|--------|---------|
| IdeCae | IdeUni |

### IR_E085SPC_007

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| EmpCon | CodEmp |
| FilCon | CodFil |

