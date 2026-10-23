# R016ORE

## Descrição

Estrutura do Organograma

---

## Resumo

- Campos: 14
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TabOrg | Number(004,0) | Não | Código da Tabela do Organograma |
| NomOrg | String(030) | Sim | Descrição do Organograma |
| UsaMas | String(001) | Sim | Usa Máscara |
| NivCol | Number(002,0) | Sim | Nível do Local p/ Cadastramento dos Colaboradores |
| NivQua | Number(002,0) | Sim | Nível do QL |
| IniDup | Date | Sim | Data de Início da Duplicação |
| HorIni | Number(005,0) | Sim | Hora de Início da Duplicação |
| FimDup | Date | Sim | Data de Término da Duplicação |
| HorFim | Number(005,0) | Sim | Hora de Término da Duplicação |
| DatAlt | Date | Sim | Data de Alteração do Organograma |
| NovOrg | Number(004,0) | Sim | Novo Organograma |
| NivFil | Number(002,0) | Sim | Nível do Local que identifica a Filial |
| NivPRA | Number(002,0) | Sim | Nível do Local p/ controle do PPRA/PCMSO |
| NivPSS | Number(002,0) | Sim | Nível do Local p/ controle do PSS |

---

## Chave Primária

- TabOrg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
