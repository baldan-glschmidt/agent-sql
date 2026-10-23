# R145DAC

## Descrição

LNT - Definições por empresa - ações disponíveis

---

## Resumo

- Campos: 9
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| SeqDac | Number(002,0) | Não | Sequencia da ação disponível para o LNT |
| DesAca | String(100) | Sim | Descrição da ação. Será exibida na tela do LNT |
| ModRel | String(011) | Sim | Modelo de relatório executado pela ação |
| CodReg | Number(003,0) | Sim | Código da regra executada pela ação |
| ExeReg | Number(001,0) | Sim | Forma de Execução da Regra |
| ConRap | String(001) | Sim | Disponibilizar ação para requisitos de aperfeiçoamento |
| ConRfo | String(001) | Sim | Disponibilizar ação para requisitos de formação |
| ConRcp | String(001) | Sim | Considerar requisitos de competência no LNT |

---

## Chave Primária

- NumEmp
- SeqDac

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
