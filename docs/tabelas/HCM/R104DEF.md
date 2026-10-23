# R104DEF

## Descrição

JR - Definições

---

## Resumo

- Campos: 7
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodOem | Number(008,0) | Sim | OBSOLETO - Código da empresa(tabela outra empresa) que é autora da ação |
| MsgVlA | String(001) | Sim | Apresentar mensagem de atualização do valor da ação ao cadastrar os pagamentos. |
| NomBot | String(020) | Sim | Nome botão para emitir sequência  de cálculo |
| ModBot | String(011) | Sim | Modelo gerador relatórios p/emitir sequência de cálculo |
| MsgAut | String(001) | Sim | Apresentar mensagem quando o autor possuir outras ações cadastradas |
| IndAtu | Number(003,0) | Sim | Define o índice a ser usado para atualização de valores |

---

## Chave Primária

- NumEmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
