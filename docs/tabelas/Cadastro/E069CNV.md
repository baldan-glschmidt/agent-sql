# E069CNV

## Descrição

Cadastros - Convênios

---

## Resumo

- Campos: 30
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCnv | Number(004,0) | Não | Código do convênio |
| DesCnv | String(050) | Não | Descrição do convênio |
| TipCnv | Number(002,0) | Não | Tipo de Convênio |
| CodCli | Number(009,0) | Não | Cliente para faturamento |
| DiaFat | Number(002,0) | Sim | Dia do mês em que encerram as vendas |
| PerSlp | Number(005,2) | Sim | Percentual de participação na ligação de convênio x produto |
| VlrSlp | Number(011,2) | Sim | Valor de participação na ligação de convênio x produto |
| LimScp | Number(015,2) | Sim | Limite do convênio ao abrir um novo período de crédito |
| LimScc | Number(015,2) | Sim | Limite para o limite de crédito do convênio do cliente |
| CreUti | Number(011,2) | Sim | Crédito Utilizado |
| LibCcl | Number(001,0) | Sim | Indicativo do momento da liberação do crédito |
| SitCnv | String(001) | Não | Situação do convênio (Ativo ou Inativo) |
| CodMot | Number(006,0) | Sim | Código do motivo da situação do convênio |
| DatVli | Date | Sim | Data de validade inicial |
| DatVlf | Date | Sim | Data de validade final |
| ObsMot | String(250) | Sim | Observação do motivo da situação do convênio |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAtu | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAtu | Date | Sim | Data da última alteração do registro |
| HorAtu | Number(005,0) | Sim | Hora da última alteração do registro |
| AplSbc | Number(001,0) | Sim | Tipo de aplicação de subsídio quando o item estiver em vários grupos |
| CodEmp | Number(004,0) | Sim | Código da empresa |
| CodTpr | String(004) | Sim | Código da tabela de preço |
| IndSen | String(001) | Sim | Indicativo se exige senha para cartão do conveniado no Varejo |
| QtdMis | Number(002,0) | Sim | Quantidade mínima de caracteres para senha do cartão do conveniado |
| QtdMas | Number(002,0) | Sim | Quantidade máxima de caracteres para senha do cartão do conveniado |
| CodCpg | String(006) | Sim | Condição de pagamento padrão do convênio. |
| DiaVen | Number(002,0) | Sim | Dia do mês em que vencem as parcelas geradas em convênio (Retaguarda) |

---

## Chave Primária

- CodCnv

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
