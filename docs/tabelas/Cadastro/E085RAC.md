# E085RAC

## Descrição

Cadastros - Clientes - Retorno Autenticadores Externo Créditos

---

## Resumo

- Campos: 15
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCli | Number(009,0) | Não | Código do cliente |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodAec | Number(004,0) | Não | Código do autenticador externo de crédito de clientes |
| SeqRac | Number(004,0) | Não | Sequência do retorno do autenticador externo de crédito de cliente |
| NumPed | Number(008,0) | Sim | Número do pedido enviado para a análise |
| DesRac | String(2499) | Sim | Descrição do retorno do autenticador externo de crédito de cliente |
| DatRac | Date | Sim | Data do retorno do autenticador externo de crédito de cliente |
| SitRac | String(001) | Não | Situação do retorno do autenticador externo de crédito de cliente |
| UsuGer | Number(010,0) | Sim | Código do usuário que gerou o registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| SeqEnv | Number(004,0) | Não | Sequência do envio do pedido para todos os autenticadores |
| MotSit | String(255) | Sim | Motivo da situação da análise de crédito do pedido |
| ParAna | String(255) | Sim | Parecer do analista de crédito |

---

## Chave Primária

- CodCli
- CodEmp
- CodFil
- CodAec
- SeqRac

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
