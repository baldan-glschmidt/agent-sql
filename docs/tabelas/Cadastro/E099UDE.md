# E099UDE

## Descrição

Cadastros - Usuários - Parâmetros Documentos Eletrônicos

---

## Resumo

- Campos: 11
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodUsu | Number(010,0) | Não | Código do usuário |
| DbuNfe | String(250) | Sim | Diretório do usuário para a geração dos boletos da nota fiscal eletrônica. |
| DbuNfs | String(250) | Sim | Diretório do usuário para a geração dos boletos da nota fiscal de serviço. |
| DbuCte | String(250) | Sim | Diretório do usuário para a geração dos boletos do conhecimento de transporte. |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- CodEmp
- CodUsu

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E099UDE_001

**Tabela:** E099USU

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodUsu | CodUsu |

