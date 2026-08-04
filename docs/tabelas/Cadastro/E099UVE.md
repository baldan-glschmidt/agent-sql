# E099UVE

## Descrição

Cadastros - Usuários - Parâmetros Vendas

---

## Resumo

- Campos: 14
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodUsu | Number(010,0) | Não | Código do usuário |
| AltTve | String(001) | Sim | Indicativo se o usuário pode alterar transação que já foi utilizada |
| PerEps | String(001) | Sim | Permissão para controlar eventos de prorrogação de suspensão de ICMS |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| CodAgr | Number(009,0) | Sim | Código responsável técnico |
| EnvRsg | String(001) | Sim | Indicativo se permite envio de receita para SIGN |
| VizSig | String(001) | Sim | Permite apenas a entrada na tela e consulta dos registros e logs do SIGA 2.0 |
| OprSig | String(001) | Sim | Habilita o botão de Reprocessar e a integração manual de pendências do SIGA 2.0 |

---

## Chave Primária

- CodEmp
- CodUsu

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E099UVE_001

**Tabela:** E099USU

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodUsu | CodUsu |

