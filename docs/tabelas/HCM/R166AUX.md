# R166AUX

## Descrição

Auxílio Educação

---

## Resumo

- Campos: 24
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Número do Colaborador |
| CmpIni | Date | Não | Competência Início da Validade do Auxílio |
| SeqAux | Number(002,0) | Não | Sequência do Auxílio |
| TipCur | String(001) | Sim | Tipo do Curso |
| CodCua | Number(009,0) | Sim | Código do Curso de Aperfeiçoamento |
| FasCua | String(003) | Sim | Fase do Curso de Aperfeiçoamento |
| CodCuf | Number(004,0) | Sim | Código do Curso de Formação |
| NivCuf | Number(002,0) | Sim | Nível de Formação do Curso |
| SeqNiv | Number(002,0) | Sim | Sequência do Nível |
| FasCuf | String(003) | Sim | Fase do Curso de Formação |
| CodOem | Number(008,0) | Sim | Código da Entidade de Ensino |
| CmpFim | Date | Sim | Competência Término da Validade do Auxílio |
| SitAux | Number(002,0) | Sim | Situação |
| DatIns | Date | Sim | Data de Inscrição |
| DatDes | Date | Sim | Data da Desativação |
| NroAta | String(020) | Sim | Ata de Aprovação |
| ObsAux | String(500) | Sim | Observação |
| CurIni | String(001) | Sim | Curso Requisitado Já Iniciado |
| IniCur | Date | Sim | Data de Início do Curso |
| FimCur | Date | Sim | Data de Fim do Curso |
| CodRee | Number(004,0) | Sim | Código do reembolso específico |
| CodMin | Number(003,0) | Sim | Código do motivo de interrupção |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CmpIni
- SeqAux

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R166AUX_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R166AUX_012

**Tabela:** R032OEM

| Origem | Destino |
|--------|---------|
| CodOem | CodOem |

