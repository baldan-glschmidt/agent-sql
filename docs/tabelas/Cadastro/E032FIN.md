# E032FIN

## Descrição

Cadastros - Financeiras

---

## Resumo

- Campos: 34
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFin | Number(004,0) | Não | Código da financeira |
| DesFin | String(100) | Não | Descrição da financeira |
| PorFin | String(004) | Não | Código interno do portador para títulos da financeira |
| PorCli | String(004) | Não | Código interno do portador para títulos do cliente |
| CodCli | Number(009,0) | Sim | Código da financeira como cliente |
| CodFor | Number(009,0) | Sim | Código da financeira como fornecedor |
| CcoFin | String(014) | Não | Número da conta interna padrão da financeira |
| PerCan | Number(005,2) | Sim | Percentual cobrado pelo cancelamento do financiamento |
| HosGat | String(255) | Sim | Host do gateway para conexão com a financeira |
| PorGat | Number(005,0) | Sim | Porta do gateway para conexão com a financeira |
| TimCon | Number(004,0) | Sim | Timeout para conexão com a financeira |
| TemRee | Number(004,0) | Sim | Tempo mínimo para reenvio da conexão com a financeira |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| CodCpg | String(006) | Sim | Código da condição de pagamento padrão da financeira |
| IndTcr | String(001) | Não | Indicativo se deve ser gerado título de controle contra o cliente |
| CodTpt | String(003) | Não | Tipo de título que devem ser gerados os títulos de controle da dívida |
| SitReg | String(001) | Não | Situação do cadastro da financeira. |
| TemRet | Number(004,0) | Sim | Tempo de Consulta de Retorno das solicitações de avaliação de crédito |
| ValCre | String(001) | Sim | Validação de Crédito é On-line |
| TptCnf | String(003) | Sim | Código do Tipo de Título para o Cancelamento do Financiamento |
| IdeUni | Number(009,0) | Não | Identificador único da financeira |
| CalPar | String(001) | Não | Tipo de cálculo das parcelas da financeira |
| CalCar | String(001) | Não | Tipo de cálculo da carência da 1ª parcela |
| PerCnc | String(001) | Sim | Indicativo se a financeira permite cancelamento de proposta financeira |
| MinPar | Number(003,0) | Sim | Mínimo de quantidade de parcelas permitido pela financeira |
| MaxPar | Number(003,0) | Sim | Máximo de quantidade de parcelas permitido pela financeira |
| MinCar | Number(003,0) | Sim | Mínimo de quantidade de dias de carência permitido pela financeira |
| MaxCar | Number(003,0) | Sim | Máximo de quantidade de dias de carência permitido pela financeira |

---

## Chave Primária

- CodEmp
- CodFin

---

## Índices

### E032FINIndice1

**Tipo:** Unico

Campos:
- IdeUni

---

## Relacionamentos

Nenhum relacionamento cadastrado.
