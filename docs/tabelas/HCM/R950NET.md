# R950NET

## Descrição

Configurações de internet

---

## Resumo

- Campos: 10
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| DatSeq | Number(004,0) | Não | Seqüência dos dados da tabela |
| UsePrx | String(001) | Sim | Indica se é pra utilizar proxy |
| PrxSrv | String(254) | Sim | Endereço do servidor proxy |
| PrxPrt | String(254) | Sim | Porta do servidor proxy |
| PrxAut | String(001) | Sim | Indica se utiliza autenticação proxy por usuário |
| PrxUsr | String(254) | Sim | Usuário padrão de proxy |
| PrxPsw | String(254) | Sim | Senha padrão de proxy |
| PrxExc | String(254) | Sim | Exceções de proxy (endereços que não usam proxy) |
| UseSsl | Number(001,0) | Sim | Indica quando é pra utilizar SSL |
| ShwPrg | String(001) | Sim | Indica se é pra exibir tela de progresso |

---

## Chave Primária

- DatSeq

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
