# R124HCN

## Descrição

Colaborador - Conhecimentos

---

## Resumo

- Campos: 30
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| FamCnc | String(004) | Não | Código da Família de Conhecimentos |
| CodCnc | String(005) | Não | Código do Conhecimento |
| SeqHcn | Number(003,0) | Não | Sequência do Conhecimento |
| DatIni | Date | Sim | Data de Início do Conhecimento |
| DatVal | Date | Sim | Data de Validade do Conhecimento |
| DatTre | Date | Sim | Data Início Treinamento |
| TipAva | Number(001,0) | Sim | Tipo do Colaborador Avaliador |
| CadAva | Number(009,0) | Sim | Cadastro do Avaliador |
| NotPrf | Number(005,2) | Sim | Nota do Conhecimento |
| PerPrf | Number(005,2) | Sim | Percentual de Conhecimento |
| NotDom | Number(005,2) | Sim | OBSOLETO 5.4.1.39 - Nota do Domínio |
| PerDom | Number(005,2) | Sim | OBSOLETO 5.4.1.39 - Percentual de Domínio |
| AprCnc | String(001) | Sim | Aprovado(S,N) |
| IdiLei | String(001) | Sim | Nível Conhecimento Leitura |
| IdiEsc | String(001) | Sim | Nível Conhecimento Escrita |
| IdiCon | String(001) | Sim | Nível Conhecimento Conversação |
| ComCnc | String(100) | Sim | Comentário sobre o Conhecimento |
| OriHCN | String(001) | Sim | Apresenta a origem do Histórico de Conhecimento |
| LotCer | Number(009,0) | Sim | Número do lote de Certificação em que foi gerado o Histórico |
| CodPro | Number(003,0) | Sim | Código da Tabela de Proficiência - OBSOLETO |
| DatPro | Date | Sim | Data da Tabela de Níveis de Proficiência - OBSOLETO |
| CodNiv | Number(002,0) | Sim | Código do Nível da Proficiência - OBSOLETO |
| CerCur | Image | Sim | Imagem do certificado do curso de conhecimento |
| CodCua | Number(009,0) | Sim | Curso |
| TmaCua | Number(006,0) | Sim | Turma |
| NumRev | Number(006,0) | Sim | Revisão |
| NomArq | String(250) | Sim | Nome do Arquivo |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- FamCnc
- CodCnc
- SeqHcn

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R124HCN_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R124HCN_004

**Tabela:** R125CNC

| Origem | Destino |
|--------|---------|
| FamCnc | FamCnc |
| CodCnc | CodCnc |

