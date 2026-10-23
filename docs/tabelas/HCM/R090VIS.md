# R090VIS

## Descrição

Visitantes

---

## Resumo

- Campos: 39
- Chave Primária: 2 campo(s)
- Índices: 2
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TipDoc | Number(001,0) | Não | Tipo do Documento do Visitante |
| NumDoc | String(020) | Não | Número do Documento do Visitante |
| NomVis | String(040) | Sim | Nome do Visitante |
| CodOem | Number(008,0) | Sim | Código da Outra Empresa |
| NomOem | String(060) | Sim | Empresa do Visitante |
| CodPrm | Number(005,0) | Sim | Código Permissão de Acesso do Visitante |
| DdiTel | Number(003,0) | Sim | Código DDI do telefone |
| DddTel | Number(003,0) | Sim | Código DDD do telefone |
| TelCon | String(020) | Sim | Número do Telefone do Visitante para Contato |
| SegTDo | Number(001,0) | Sim | Segundo Tipo do Documento do Visitante |
| SegDoc | String(020) | Sim | Segundo Número do Documento do Visitante |
| NumCnh | String(020) | Sim | Número da Carteira de Habilitação |
| CatCnh | String(004) | Sim | Categoria da Carteira de Habilitação |
| DatCnh | Date | Sim | Data da Primeira Habilitação |
| VenCnh | Date | Sim | Data de Vencimento da Carteira de Habilitação |
| ObsVis | String(160) | Sim | Observação do Visitante |
| FotVis | Image | Sim | Foto do Visistante |
| DatVid | Date | Sim | Data em que o Visitante Assistiu ao Vídeo de Segurança |
| DatFot | Date | Sim | Data da Foto |
| FlaFot | Number(001,0) | Sim | Flag da Foto |
| DatRgv | Date | Sim | Data em que o visitante recebeu o guia de segurança |
| EmiCid | String(020) | Sim | Orgão Emissor da Carteira de Identidade |
| EstCid | String(002) | Sim | Estado do Orgão Emissor da Carteira de Identidade |
| DexCid | Date | Sim | Data de Expedição da Carteira de Identidade |
| ConTpm | String(001) | Sim | Controla tempo de permanência |
| CodNac | Number(003,0) | Sim | Código da Nacionalidade |
| UtiChv | String(001) | Sim | Pode usar chave |
| SeqReg | Number(015,0) | Sim | Sequencia do Registro |
| EmaVis | String(100) | Sim | E-mail do Visitante |
| DatIdx | Date | Sim | Data da indexação da foto para reconhecimento facial |
| NomDoc | String(040) | Sim | Nome do visitante contido no documento |
| DatNas | Date | Sim | Data de Nascimento |
| FunVis | String(060) | Sim | Função do visitante na empresa representada |
| QuaVis | String(060) | Sim | Qualificação do visitante na empresa representada |
| StaAlf | Number(001,0) | Sim | Status da permissão para o local alfandegado |
| DvaDoc | Date | Sim | Data de Validade (Documento) |
| PaiDoc | Number(004,0) | Sim | País de Emissão (Documento) |
| TipSex | String(001) | Sim | Sexo do Visitante |
| HorFot | Number(005,0) | Sim | Hora da Foto |

---

## Chave Primária

- TipDoc
- NumDoc

---

## Índices

### R090VISIndice2

**Tipo:** Não unico

Campos:
- NomVis

### R090VISIndice3

**Tipo:** Não unico

Campos:
- SegTDo
- SegDoc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
