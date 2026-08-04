# E024MSG

## Descrição

Tabelas - Mensagens para Nota Fiscal de Saída e Contrato de Venda

---

## Resumo

- Campos: 16
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodMsg | Number(004,0) | Não | Código da mensagem especial para nota fiscal de saída e contrato |
| DesMsg | String(1000) | Não | Texto da mensagem especial para nota fiscal de saída e contrato |
| StrFed | String(005) | Sim | Código da situação tributária federal para impostos |
| RotApl | Number(002,0) | Sim | Rotina em que será aplicada a mensagem especial |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração da mensagem |
| DatGer | Date | Sim | Data da geração da mensagem |
| HorGer | Number(005,0) | Sim | Hora da geração da mensagem |
| MsgFis | String(001) | Sim | Indicativo se a mensagem é fiscal |
| NumPrf | String(255) | Sim | Número do processo ou ato concessório |
| OriPrf | Number(001,0) | Sim | Origem do processo ou ato concessório |
| DocRef | Number(002,0) | Sim | Documento Referenciado |
| MsgDin | Number(004,0) | Sim | Código da mensagem especial para nota fiscal de saída e contrato |
| EntDin | String(010) | Sim | Entidade dinâmica |
| DesMsd | String(1000) | Sim | Texto da mensagem especial para nota fiscal de saída e contrato |
| IntMsg | String(001) | Sim | Indicativo para especificar o interessado da mensagem |
| TipAtc | Number(002,0) | Sim | Tipo do ato concessório |

---

## Chave Primária

- CodMsg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
