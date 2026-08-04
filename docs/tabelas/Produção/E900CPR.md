# E900CPR

## Descrição

O.P./O.S. - Controle processos de remessa para terceiros via WS

---

## Resumo

- Campos: 19
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| NumPrc | Number(009,0) | Não | Número sequencial do processo de remessa para terceiros |
| DtiPrc | Date | Sim | Data de início do processo de remessa para terceiros |
| HriPrc | Number(005,0) | Sim | Hora de início do processo de remessa para terceiros |
| SitPrc | String(001) | Sim | Situação do processo de remessa para terceiros |
| SitRem | String(001) | Sim | Situação da remessa das OPs |
| SitBxa | String(001) | Sim | Situação da baixa dos componentes |
| SitGnf | String(001) | Sim | Situação da geração da nota fiscal de remessa |
| MsgPrc | String(255) | Sim | Mensagem de retorno do processo de remessa para terceiros |
| RelStr | String(180) | Sim | Relatórios de Produção utilizados no processo de remessa para terceiros |
| OriStr | String(100) | Sim | Origens utilizadas no processo de remessa para terceiros |
| CodEtg | Number(004,0) | Não | Estágio de produção utilizado no processo de remessa para terceiros |
| CodFor | Number(009,0) | Sim | Fornecedor utilizado no processo de remessa para terceiros |
| BxaCmp | String(001) | Sim | Indicativo se baixa os componentes |
| PreNfr | String(001) | Sim | Indicativo se prepara nota fiscal de remessa |
| AdiPro | String(001) | Sim | Indicativo se adiciona produto na nota fiscal de remessa |
| CodUsu | Number(010,0) | Sim | Usuário responsável pela geração do processo de remessa |
| CmpSpa | String(001) | Sim | Indicativo se remete apenas os componentes que foram separados |
| TipRst | Number(001,0) | Não | Tipo remessa de serviço para terceiros |

---

## Chave Primária

- CodEmp
- NumPrc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E900CPR_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

