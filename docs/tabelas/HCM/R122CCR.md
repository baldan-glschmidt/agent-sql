# R122CCR

## Descrição

Candidatos Externos - Cursos Aperfeiçoamento

---

## Resumo

- Campos: 22
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumCan | Number(007,0) | Não | Cadastro Candidato |
| CodCua | Number(009,0) | Não | Código do Curso |
| SeqCcr | Number(004,0) | Não | Sequência do Curso Aperfeiçoamento |
| PerIni | Date | Sim | Data Início |
| PerFim | Date | Sim | Data Fim |
| CodOem | Number(008,0) | Sim | Código Entidade |
| NomOem | String(060) | Sim | Nome da entidade de ensino |
| SitCua | Number(002,0) | Sim | Situação Curso |
| TipCer | String(001) | Sim | Tipo do Certificado |
| MedCua | Number(005,2) | Sim | Média Curso |
| FreCua | Number(005,2) | Sim | Frequência Curso |
| CarHor | Number(010,0) | Sim | Carga Horária |
| FasCua | String(003) | Sim | Fase do Curso de Aperfeiçoamento |
| ComCua | String(250) | Sim | Comentário Formação Curso |
| IndVct | String(001) | Sim | Indicador Curso Vencido |
| IdiLei | String(001) | Sim | Nível Conhecimento Leitura |
| IdiEsc | String(001) | Sim | Nível Conhecimento Escrita |
| IdiCon | String(001) | Sim | Nível Conhecimento Conversação |
| CodMin | Number(003,0) | Sim | Código do motivo de interrupção |
| NomCua | String(200) | Sim | Nome do Curso |
| SeqCAP | Number(006,0) | Sim | Sequência do Curso Aperfeiçoamento |
| OriInf | Number(001,0) | Sim | Origem da informação do curso |

---

## Chave Primária

- NumCan
- CodCua
- SeqCcr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R122CCR_000

**Tabela:** R122CEX

| Origem | Destino |
|--------|---------|
| NumCan | NumCan |

### IR_R122CCR_001

**Tabela:** R128CUA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |

