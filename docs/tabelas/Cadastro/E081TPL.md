# E081TPL

## Descrição

Tabelas - Tabelas de Preços de Venda - Ligação com Filiais

---

## Resumo

- Campos: 20
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodTpr | String(004) | Não | Código da tabela de preço |
| CodFil | Number(005,0) | Não | Código da filial |
| DesTpr | String(250) | Sim | Descrição da tabela de preço |
| NomFil | String(100) | Sim | Razão social da filial da empresa |
| SigFil | String(030) | Sim | Nome fantasia da filial da empresa |
| AbrTpr | String(010) | Sim | Abreviatura da tabela de preço |
| CodMoe | String(003) | Sim | Código da moeda que os preço dos produtos/serviços estão representados |
| EspCli | String(001) | Sim | Indicativo se a tabela é especial para cliente |
| AplTpv | Number(001,0) | Sim | Aplicação da tabela de preço de venda |
| SitReg | String(001) | Sim | Situação do registro |
| IndExp | Number(001,0) | Sim | Indicativo se o registro foi alterado para exportar para o palm |
| DatPal | Date | Sim | Data da última alteração para o Palmtop |
| HorPal | Number(005,0) | Sim | Hora/minuto da última alteração para o Palm |
| UtiPme | String(001) | Sim | Indicativo se utiliza preço médio como preço base dos itens da tabela de preço |
| CodPdv | Number(010,0) | Sim | Código interno no PDV |
| CodCli | Number(009,0) | Sim | Código do cliente que poderá utilizar a tabela de preço |
| CodTpb | String(004) | Sim | Código da tabela de preço base |
| VenEcf | String(001) | Sim | Indicativo se a tabela será utilizada para venda com ECF |
| TabBld | String(001) | Sim | Indicativo se a tabela de preço é um tablóide |

---

## Chave Primária

- CodEmp
- CodTpr
- CodFil

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E081TPL_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

