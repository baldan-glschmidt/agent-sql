# R166DEF

## Descrição

Definições - Auxílio

---

## Resumo

- Campos: 13
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CheTet | String(001) | Sim | Checar Teto nos Lançamentos |
| VlrRee | String(001) | Sim | Tratamento do Valor Reembolso |
| QtdMes | Number(002,0) | Sim | Meses anteriores a ser mostrado no lançamento do auxílio |
| SugVlr | String(001) | Sim | Sugere valor informado p/item de custo como despesa |
| InfRee | String(001) | Sim | Informa reembolso por data completa ou por competência |
| ModBo1 | String(011) | Sim | Modelo Gerador Relatórios do 1º Botão |
| ModBo2 | String(011) | Sim | Modelo Gerador Relatórios do 2º Botão |
| NomBo1 | String(020) | Sim | Nome do 1º Botão |
| NomBo2 | String(020) | Sim | Nome do 2º Botão |
| RegBo1 | Number(003,0) | Sim | Código da regra do 1º botão |
| RegBo2 | Number(003,0) | Sim | Código da regra do 2º botão |
| LimTel | String(001) | Sim | Manter lançamentos visíveis após gravação na tela de lançamento de despesas |

---

## Chave Primária

- NumEmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R166DEF_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

