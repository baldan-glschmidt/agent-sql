# E085CAE

## Descrição

Cadastros - Clientes - Consultas de Autenticadores Externos de Créditos

---

## Resumo

- Campos: 16
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodAec | Number(004,0) | Não | Código do autenticador externo de crédito de clientes |
| CodCae | Number(004,0) | Não | Código da consulta do autenticador externo de crédito de clientes |
| DesCae | String(100) | Sim | Descrição da consulta do autenticador externo de crédito de clientes |
| DisFis | String(001) | Sim | Indicativo se está disponível para pessoa física |
| DisJur | String(001) | Sim | Indicativo se está disponível para pessoa jurídica |
| UrlSec | String(200) | Sim | URL dos serviços de consulta |
| TplReq | String(50000) | Sim | Template da requisição |
| TplRes | String(50000) | Sim | Template da resposta |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- IdeUni

---

## Índices

### E085CAE_UNIQUE

**Tipo:** Unico

Campos:
- CodEmp
- CodAec
- CodCae

---

## Relacionamentos

### IR_E085CAE_002

**Tabela:** E085AEC

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodAec | CodAec |

