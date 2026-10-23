# R033HAP

## Descrição

Histórico de Cursos de Aperfeiçoamento da Pessoa

---

## Resumo

- Campos: 34
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPes | Number(009,0) | Não | Código da Pessoa |
| SeqCAP | Number(006,0) | Não | Sequência do Curso Aperfeiçoamento |
| CodCua | Number(009,0) | Sim | Código do Curso |
| PerIni | Date | Sim | Data Inicial |
| PerFim | Date | Sim | Data Final |
| CodOem | Number(008,0) | Sim | Código Entidade |
| NomOem | String(060) | Sim | Nome da entidade de ensino |
| SitCua | Number(002,0) | Sim | Situação do Curso |
| TipCer | String(001) | Sim | Tipo de Certificado |
| MedCua | Number(005,2) | Sim | Média do Curso |
| FreCua | Number(005,2) | Sim | Frequência do Curso |
| CarHor | Number(010,0) | Sim | Carga Horária |
| FasCua | String(003) | Sim | Fase do Curso de Aperfeiçoamento |
| ComCua | String(250) | Sim | Comentário do curso de aperfeiçoamento |
| IndVct | String(001) | Sim | Indicador de Curso Vencido |
| IdiLei | String(001) | Sim | Nível Conhecimento Leitura |
| IdiEsc | String(001) | Sim | Nível Conhecimento Escrita |
| IdiCon | String(001) | Sim | Nível Conhecimento Conversação |
| OriHcr | String(001) | Sim | Origem do Histórico Cursos Aperfeiçoamento |
| IdiCua | String(001) | Sim | Forma de aquisição do curso |
| TmaCua | Number(006,0) | Sim | Código da Turma relacionada ao histórico |
| CodEvn | Number(009,0) | Sim | Código do Evento |
| CodMin | Number(003,0) | Sim | Código do motivo de interrupção |
| CerCur | Image | Sim | Imagem do certificado do curso de aperfeiçoamento |
| NomCua | String(200) | Sim | Nome do Curso |
| NomArq | String(250) | Sim | Nome do certificado em anexo |
| EmpAux | Number(004,0) | Sim | USO EXCLUSIVO SENIOR |
| TipAux | Number(001,0) | Sim | USO EXCLUSIVO SENIOR |
| CadAux | Number(009,0) | Sim | USO EXCLUSIVO SENIOR |
| DepAux | Number(002,0) | Sim | USO EXCLUSIVO SENIOR |
| ColAti | Number(001,0) | Sim | USO EXCLUSIVO SENIOR |
| CanAux | Number(007,0) | Sim | USO EXCLUSIVO SENIOR |
| DatAux | Date | Sim | USO EXCLUSIVO SENIOR |
| TipTre | Number(001,0) | Sim | Tipo do treinamento/capacitação |

---

## Chave Primária

- CodPes
- SeqCAP

---

## Índices

### R033HAPIndice2

**Tipo:** Não unico

Campos:
- CodPes
- CodCua
- PerIni

---

## Relacionamentos

### IR_R033HAP_000

**Tabela:** R033PES

| Origem | Destino |
|--------|---------|
| CodPes | CodPes |

### IR_R033HAP_002

**Tabela:** R128CUA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |

