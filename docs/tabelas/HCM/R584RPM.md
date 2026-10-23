# R584RPM

## Descrição

Manutenção do Inventário de Riscos - Responsáveis

---

## Resumo

- Campos: 10
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodInv | Number(007,0) | Não | Código do Inventário de Riscos |
| NumAmb | Number(007,0) | Não | Código do Ambiente de Trabalho |
| DatInv | Date | Não | Data do Inventário de Riscos |
| CodPes | Number(009,0) | Não | Código da Pessoa |
| RspEla | String(001) | Sim | Informar se é um responsável pela elaboração |
| RspLeg | String(001) | Sim | Informar se é um responsável legal |
| RspTec | String(001) | Sim | Informar se é um responsável técnico |
| RspSst | String(001) | Sim | Informar se é um responsável pela Segurança e Saúde no Trabalho |
| RspAss | String(001) | Sim | Informar se o responsável deve assinar no Inventário de Riscos |
| FunRsp | String(100) | Sim | Função do responsável |

---

## Chave Primária

- CodInv
- NumAmb
- DatInv
- CodPes

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
