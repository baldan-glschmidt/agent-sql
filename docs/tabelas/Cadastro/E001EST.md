# E001EST

## Descrição

Tabelas - Transações - Estoques

---

## Resumo

- Campos: 11
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodTns | String(005) | Não | Código da transação |
| TmeSpe | String(002) | Sim | Tipo de Movimento de Entrada de Estoque para o controle do Sped Fiscal |
| TmsSpe | String(002) | Sim | Tipo de Movimento de Saída de Estoque para o controle do Sped Fiscal |
| CalMmf | String(001) | Sim | Indicativo se a transação calcula Média Fixa Mensal |
| DepTns | String(001) | Sim | Indicativo se é obrigatória a ligação do depósito X transação |
| GerMvp | String(001) | Sim | Indicativo se a transação gera movimento de estoque |
| TpdFre | String(001) | Sim | Indicativo se é transação padrão para movimentação de frete |
| RccNap | String(001) | Sim | Considerar no SPED para ratear o consumo de componente não apontado na produção |
| CodCoa | Number(005,0) | Sim | Código do Cadastro de Operações |
| ParEma | String(001) | Sim | Participa da análise de estoque mínimo automatizado |

---

## Chave Primária

- CodEmp
- CodTns

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E001EST_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

### IR_E001EST_001

**Tabela:** E001TNS

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodTns | CodTns |

