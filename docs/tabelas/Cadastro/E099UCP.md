# E099UCP

## Descrição

Cadastros - Usuários - Parâmetros Compras

---

## Resumo

- Campos: 12
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodUsu | Number(010,0) | Não | Código do usuário |
| AltTcp | String(001) | Sim | Indicativo se o usuário pode alterar transação que já foi utilizada |
| OpcCtr | String(001) | Sim | Indicativo se usuário pode vincular/desvincular contrato à OC na tela F460CXO |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| RepFix | String(001) | Sim | Permitir a alteração de representante na fixação |
| AceHry | String(001) | Sim | Acesso tela de gestão do HUB de Royalties |

---

## Chave Primária

- CodEmp
- CodUsu

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E099UCP_001

**Tabela:** E099USU

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodUsu | CodUsu |

