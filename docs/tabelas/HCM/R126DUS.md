# R126DUS

## Descrição

Definições do Recrutamento por Usuário

---

## Resumo

- Campos: 20
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodUsu | Number(010,0) | Não | Código do Usuário |
| IntAge | Number(002,0) | Sim | Intervalo em Minutos |
| ExiSeg | String(001) | Sim | Exibir na Agenda Segunda-Feira |
| ExiTer | String(001) | Sim | Exibir na Agenda Terça-Feira |
| ExiQua | String(001) | Sim | Exibir na Agenda Quarta-Feira |
| ExiQui | String(001) | Sim | Exibir na Agenda Quinta-Feira |
| ExiSex | String(001) | Sim | Exibir na Agenda Sexta-Feira |
| ExiSab | String(001) | Sim | Exibir na Agenda Sábado |
| ExiDom | String(001) | Sim | Exibir na Agenda Domingo |
| InfSal | String(001) | Sim | Permite Informar Salário na Requisição |
| SalSVa | String(001) | Sim | Permite Informar Salário na Solicitação |
| ExiAbe | String(001) | Sim | Mostrar Requisições Abertas |
| ExiCan | String(001) | Sim | Mostrar Requisições Canceladas |
| ExiSus | String(001) | Sim | Mostrar Requisições Suspensas |
| ExiFin | String(001) | Sim | Mostrar Requisições Finalizadas |
| AbrRes | String(100) | Sim | Abrangência de  Responsável de Requisição |
| PerPro | String(001) | Sim | Permite Processos(Triagem/Manut./Efet.) sobre Requições de outro Responsável |
| PerMan | String(001) | Sim | Permite Manutenção(Requisição/Requisitos) sobre Requições de outro Responsável |
| AbrSit | String(020) | Sim | Abrangência de Situação do Candidato |
| ASaSVa | String(001) | Sim | Permite alterar Salário nas Solicitações criadas por outros usuários |

---

## Chave Primária

- CodUsu

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
