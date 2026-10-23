# R124HCR

## Descrição

Colaborador - Cursos Aperfeiçoamento

---

## Resumo

- Campos: 30
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CodCua | Number(009,0) | Não | Código do Curso |
| SeqHcr | Number(004,0) | Não | Sequência do Curso Aperfeiçoamento |
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
| ComCua | String(250) | Sim | Comentário Formacão do Curso |
| IndVct | String(001) | Sim | Indicador de Curso Vencido |
| IdiLei | String(001) | Sim | Nível Conhecimento Leitura |
| IdiEsc | String(001) | Sim | Nível Conhecimento Escrita |
| IdiCon | String(001) | Sim | Nível Conhecimento Conversação |
| OriHcr | String(001) | Sim | Origem do Histórico Cursos Aperfeiçoamento |
| IdiCua | String(001) | Sim | Forma de aquisição do curso |
| TmaCua | Number(006,0) | Sim | Código da Turma relacionada ao histórico |
| CodMin | Number(003,0) | Sim | Código do motivo de interrupção |
| CerCur | Image | Sim | Imagem do certificado do curso de aperfeiçoamento |
| NomCua | String(200) | Sim | Nome do Curso |
| SeqCAP | Number(006,0) | Sim | Sequência do Curso Aperfeiçoamento |
| OriInf | Number(001,0) | Sim | Origem da informação do curso |
| NomArq | String(250) | Sim | Nome do Arquivo |
| TipTre | Number(001,0) | Sim | Tipo do treinamento/capacitação |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodCua
- SeqHcr

---

## Índices

### R124HCRIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- TipCol
- NumCad
- CodCua
- PerIni

---

## Relacionamentos

### IR_R124HCR_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R124HCR_003

**Tabela:** R128CUA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |

