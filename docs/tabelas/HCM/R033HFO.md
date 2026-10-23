# R033HFO

## Descrição

Histórico de Cursos de Formação da Pessoa

---

## Resumo

- Campos: 31
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPes | Number(009,0) | Não | Código da Pessoa |
| SeqCFP | Number(006,0) | Não | Sequência do Curso Formação |
| CodCuf | Number(004,0) | Sim | Código do Curso |
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
| NomArq | String(250) | Sim | Nome do Certificado em anexo |
| EmpAux | Number(004,0) | Sim | USO EXCLUSIVO SENIOR |
| TipAux | Number(001,0) | Sim | USO EXCLUSIVO SENIOR |
| CadAux | Number(009,0) | Sim | USO EXCLUSIVO SENIOR |
| DepAux | Number(002,0) | Sim | USO EXCLUSIVO SENIOR |
| ColAti | Number(001,0) | Sim | USO EXCLUSIVO SENIOR |
| CanAux | Number(007,0) | Sim | USO EXCLUSIVO SENIOR |
| DatAux | Date | Sim | USO EXCLUSIVO SENIOR |

---

## Chave Primária

- CodPes
- SeqCFP

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R033HFO_000

**Tabela:** R033PES

| Origem | Destino |
|--------|---------|
| CodPes | CodPes |

### IR_R033HFO_002

**Tabela:** R127CUF

| Origem | Destino |
|--------|---------|
| CodCuf | CodCuf |

