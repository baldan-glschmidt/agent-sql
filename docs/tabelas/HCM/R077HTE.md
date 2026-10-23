# R077HTE

## Descrição

Habilidades Técnicas

---

## Resumo

- Campos: 28
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodHte | String(006) | Não | Código da Habilidade Técnica |
| NomHte | String(100) | Sim | Nome da Habilidade |
| GraCpx | String(001) | Sim | Grau de Complexidade da Habilidade |
| DatRev | Date | Sim | Data da Revisão |
| DatTer | Date | Sim | Data Término da Validade |
| NumRev | String(010) | Sim | Número da Revisão |
| MesVal | Number(003,0) | Sim | Meses Validade |
| ObsHge | String(080) | Sim | Observação |
| DesHge | String(5000) | Sim | Descrição da Habilidade |
| CodTbn | Number(003,0) | Sim | Código da Tabela de Notas |
| NotPrf | Number(005,2) | Sim | Nota Mínima de Performance |
| PerPrf | Number(005,2) | Sim | %  Mínimo Performance |
| PesPrf | Number(002,0) | Sim | Peso da Performance |
| TesPra | Number(005,0) | Sim | Grupo de Perguntas do Teste Prático |
| TesTeo | Number(005,0) | Sim | Grupo de Perguntas do Teste Teórico |
| NotDom | Number(005,2) | Sim | OBSOLETO 5.4.1.39 - Nota Mínima de Conhecimento |
| PerDom | Number(005,2) | Sim | %  Mínimo Conhecimento |
| PesDom | Number(002,0) | Sim | Peso do Conhecimento |
| PerApf | Number(005,2) | Sim | % Aperfeiçoamento |
| PesCua | Number(002,0) | Sim | Peso dos Cursos de Aperfeiçoamento |
| PerFor | Number(005,2) | Sim | % Formação |
| PesCuf | Number(002,0) | Sim | Peso dos Cursos de Formação |
| UtiAva | String(001) | Sim | Define se a Habilidade é utilizada na Avaliação |
| UtiCer | String(001) | Sim | Define se a Habilidade é utilizada na Certificação |
| AuxAva | String(001) | Sim | Define se esta Habilidade pode auxiliar uma Avaliação |
| CodAva | Number(004,0) | Sim | Código da avaliação detalhada |
| OriCeH | String(001) | Sim | Define como a Habilidade é Certificada (pela Avaliação, Testes ou Requisitos) |
| NomArq | String(250) | Sim | Arquivo |

---

## Chave Primária

- CodHte

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
