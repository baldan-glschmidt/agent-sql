# E070EPR

## Descrição

Cadastros - Empresas - Parâmetros para Manufatura e Serviços

---

## Resumo

- Campos: 18
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| UtiNor | String(001) | Não | Indicador se utiliza o nível da origem para definir árvore hierárquica do produto acabado final |
| PrdMul | String(001) | Não | Utiliza cálculo de explosão de Necessidades encadeado (Multinível) |
| ConDig | String(001) | Não | Considera O.Ps. digitadas na quantidade de ordens do estoque (influencia na quantidade disponível) |
| GerCor | String(001) | Não | Gera calendário ocupação dos recursos da OP |
| GerOpc | String(001) | Sim | Gera todas as opções das operações nas OPs/OSs |
| SerMnc | String(014) | Sim | Código do serviço para manutenções corretivas |
| TnsMnt | String(005) | Sim | Transação padrão para movimentações saída de estoque geradas por manutenções |
| TnsSrv | String(005) | Sim | Transação de manutenção para solicitação de compras de serviço |
| CrrMnt | String(001) | Sim | Indicativo se confirma o recebimento dos materiais requisitados para manutenção |
| IndPre | String(001) | Não | Indicativo de ativação de parada por equipamento |
| CcuMnt | String(009) | Sim | Código do centro de custos padrão de execução de manutenção |
| CcuMfr | String(009) | Sim | Código do centro de custos padrão de execução de manutenção de ferramentas |
| MprDse | String(004) | Sim | Motivo da parada gerada por desuso de equipamento/ferramenta |
| DurDse | Number(006,0) | Sim | Duração prevista da parada gerada por desuso de equip./ferram. (em minutos) |
| TnsIcp | String(005) | Sim | Transação para saída de estoque na incorporação de produtos na OP |
| NfsRem | String(001) | Não | Indicativo se o sistema irá sugerir automaticamente geração de NF de remessa |
| InaMod | String(001) | Sim | Indicativo se inativa o Modelo quando houver modificação em campo de usuário |

---

## Chave Primária

- CodEmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
