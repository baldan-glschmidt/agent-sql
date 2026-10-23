# R124HCF

## Descrição

Colaborador - Cursos Formação

---

## Resumo

- Campos: 28
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CodCuf | Number(004,0) | Não | Código do Curso |
| SeqHcf | Number(002,0) | Não | Sequência do Curso Formação |
| PerIni | Date | Sim | Data Inicial |
| PerFim | Date | Sim | Data Final |
| DatPrv | Date | Sim | Data de Previsão para Conclusão |
| CodOem | Number(008,0) | Sim | Código Entidade |
| SitCuf | Number(002,0) | Sim | Situação do Curso |
| NivCuf | Number(002,0) | Sim | Nível de Formação do Curso |
| SeqNiv | Number(002,0) | Sim | Sequência do Nível |
| FasCuf | String(003) | Sim | Fase do Curso de Formação |
| ComCuf | String(500) | Sim | Comentário Formacão do Curso |
| CodAcn | Number(008,0) | Sim | Área de Conhecimento |
| MecReg | String(010) | Sim | Registro do Diploma no MEC - Número |
| MecFol | String(010) | Sim | Registro do Diploma no MEC - Folhas |
| MecLiv | String(010) | Sim | Registro do Diploma no MEC - Livro |
| MecDat | Date | Sim | Registro do Diploma no MEC - Data |
| TitTes | String(200) | Sim | Título da Tese |
| TitObt | String(059) | Sim | Título obtido através desse curso |
| CodMin | Number(003,0) | Sim | Código do motivo de interrupção |
| CerCur | Image | Sim | Imagem do certificado do curso de formação |
| NomOem | String(060) | Sim | Nome da Entidade de Ensino |
| NomCuf | String(060) | Sim | Nome do Curso de Formação |
| SeqCFP | Number(006,0) | Sim | Sequência do Curso Formação |
| OriInf | Number(001,0) | Sim | Origem da informação do curso |
| NomArq | String(250) | Sim | Nome do Arquivo |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodCuf
- SeqHcf

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R124HCF_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R124HCF_003

**Tabela:** R127CUF

| Origem | Destino |
|--------|---------|
| CodCuf | CodCuf |

