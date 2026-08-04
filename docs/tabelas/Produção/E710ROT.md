# E710ROT

## Descrição

Ficha - Roteiro - Dados Gerais

---

## Resumo

- Campos: 37
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodRot | String(014) | Não | Código do Roteiro de Produção associado ao Produto |
| DesRot | String(100) | Sim | Descrição do Roteiro de Produção |
| CodFam | String(006) | Não | Código da Família de Produto ao qual o Roteiro pertence |
| TmpObt | Number(008,2) | Não | Tempo de Produção, em dias, proporcional ao lote técnico a produzir |
| TmpFix | Number(008,2) | Não | Tempo Fixo em Dias |
| LotTec | Number(010,3) | Não | Quantidade do Lote Técnico ideal, para a fabricação do Produto |
| SitRot | String(001) | Não | Situação do Roteiro (A=Ativo, I=Inativo) |
| UsoCus | String(001) | Sim | Já foi utilizado p/ formação de preço de Custos? (S=Sim, N=Não) |
| QtdBas | Number(014,5) | Não | Quantidade Base em relação aos tempos informados |
| DatGer | Date | Sim | Data de Geração do Roteiro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuGer | Number(010,0) | Sim | Código do usuário responsável pelo geração do registro |
| DatAlt | Date | Não | Data da Geração/Alteração do Roteiro p/ Controle (Custos) |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| UsuAlt | Number(010,0) | Sim | Código do usuário responsável pelo alteração do registro |
| VerRot | String(015) | Sim | Última versão do roteiro na qual é incrementada em cada nova alteração |
| RotAnx | Number(002,0) | Sim | Código da rotina para controle de arquivos anexos |
| NumAnx | Number(010,0) | Sim | Número do controle de arquivos anexos gerado pelo sistema |
| USU_Aprova | String(020) | Sim | Nome do Aprovador do Processo |
| USU_Elabor | String(020) | Sim | Nome do Elaborador do Processo |
| USU_Dtelab | Date | Sim | Data de Elaboracao do Processo |
| USU_Revpro | Number(002,0) | Sim | Numero de Revisao do Processo |
| USU_Dtrep | Date | Sim | Data de Revisao do Processo |
| USU_Revdes | Number(002,0) | Sim | Numero da Revisao do Desenho |
| USU_Dtrevd | Date | Sim | Data de Revisao do Desenho |
| USU_Hispro | String(240) | Sim | Historico da Ultima Revisao do Processo |
| USU_prores | String(001) | Sim | Pocesso Revisado |
| USU_Arqvar | String(040) | Sim | Identificacao do Arquivo e/ou Varal para Implantacao |
| USU_Hispro2 | String(250) | Sim | Historico da Ultima Revisao do Processo |
| USU_Dtapro | Date | Sim | Data de Aprovacao do Processo |
| USU_dtrepb | Date | Sim | Data Revisao Peso Bruto |
| USU_cronom | String(001) | Sim | Cronometrado |
| USU_sequen | String(120) | Sim | Seq. Cronometrada Tempo Ciclo |
| USU_datcro | Date | Sim | Data Cronometrado |
| USU_seq_setup | String(120) | Sim | Seq. Cronometrada Tempo Setup |
| USU_seq_total | String(120) | Sim | Seq. Cronometrada (Setup + Tempo Ciclo) |

---

## Chave Primária

- CodEmp
- CodRot

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E710ROT_003

**Tabela:** E012FAM

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFam | CodFam |

